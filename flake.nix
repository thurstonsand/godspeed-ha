{
  description = "Godspeed/Home Assistant Integration Development Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    git-hooks-nix = {
      url = "github:cachix/git-hooks.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = inputs @ {
    nixpkgs,
    flake-parts,
    ...
  }:
    flake-parts.lib.mkFlake {inherit inputs;} {
      imports = [
        inputs.git-hooks-nix.flakeModule
      ];
      systems = ["x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin"];
      perSystem = {
        config,
        pkgs,
        system,
        ...
      }: let
        venvDir = "./.venv";
      in {
        formatter = pkgs.alejandra;

        # Configure pre-commit hooks
        pre-commit.settings = {
          excludes = ["custom_components/old_godspeed"]; # TODO: Remove this exclusion once old_godspeed folder is deleted
          hooks = {
            ruff = {
              enable = true;
              types = ["python"];
            };
            ruff-format = {
              enable = true;
              types = ["python"];
            };
            check-added-large-files.enable = true;
            check-yaml.enable = true;
            end-of-file-fixer.enable = true;
            trim-trailing-whitespace.enable = true;
          };
        };

        devShells.default = let
          python = pkgs.python313;
          pythonPackages = python.pkgs;
        in
          pkgs.mkShell rec {
            inherit venvDir;
            nativeBuildInputs = with pkgs;
              [
                alejandra
              ]
              ++ (with pythonPackages; [
                venvShellHook
                virtualenv
              ]);
            postVenvCreation = ''
              python -m pip install -r ./requirements_test.txt --upgrade
            '';
            shellHook = ''
              venvShellHook

              # only install requirements if they have changed
              git diff --quiet requirements_test.txt requirements_dev.txt || pip install -r requirements_test.txt

              ${config.pre-commit.installationScript}

              echo "Godspeed development environment ready."
              echo "Run 'pfmt'/'ptest' to format/test your code"
            '';

            postShellHook = ''
              # Define format command
              if [ ! -f "${venvDir}/bin/pfmt" ]; then
                echo "#!/usr/bin/env bash
              pre-commit run --all-files" > "${venvDir}/bin/pfmt"
                chmod +x "${venvDir}/bin/pfmt"
              fi

              # Define test command
              if [ ! -f "${venvDir}/bin/ptest" ]; then
                echo "#!/usr/bin/env bash
              pytest --timeout=9 --durations=10 -n auto tests" > "${venvDir}/bin/ptest"
                chmod +x "${venvDir}/bin/ptest"
              fi

              ln -sf ${python.sitePackages}/* "${venvDir}/lib/python3.13/site-packages"
            '';
          };
      };
    };
}
