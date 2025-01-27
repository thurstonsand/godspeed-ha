# Source: https://developers.home-assistant.io/docs/core/integration-quality-scale/

## URL: https://developers.home-assistant.io/docs/core/integration-quality-scale/

Title: Integration quality scale | Home Assistant Developer Docs

URL Source: https://developers.home-assistant.io/docs/core/integration-quality-scale/

Markdown Content:
The integration quality scale is a framework for Home Assistant to grade integrations based on user experience, features, code quality and developer experience. To grade this, the project has come up with a set of tiers, which all have their own meaning.

## Scaled tiers[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#scaled-tiers "Direct link to Scaled tiers")

There are 4 scaled tiers, bronze, silver, gold, and platinum. To reach a tier, the integration must fulfill all rules of that tier and the tiers below.

These tiers are defined as follows.

### 🥉 Bronze[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#-bronze "Direct link to 🥉 Bronze")

The bronze tier is the baseline standard and requirement for all new integrations. It meets the minimum requirements in code quality, functionality, and user experience. It complies with the fundamental expectations and provides a reliable foundation for users to interact with their devices and services.

The documentation provides guidelines for setting up the integration directly from the Home Assistant user interface.

From a technical perspective, this integration has been reviewed to comply with all baseline standards, which we require for all new integrations, including automated tests for setting up the integration.

The bronze tier has the following characteristics:

- Can be easily set up through the UI.
- The source code adheres to basic coding standards and development guidelines.
- Automated tests that guard this integration can be configured correctly.
- Offers basic end-user documentation that is enough to get users started step-by-step easily.

### 🥈 Silver[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#-silver "Direct link to 🥈 Silver")

The silver tier builds upon the “Bronze” level by improving the reliability and robustness of integrations, ensuring a solid runtime experience. It ensures an integration handles errors properly, such as when authentication to a device or service fails, handles offline devices, and other errors.

The documentation for these integrations provides information on what is available in Home Assistant when this integration is used, as well as troubleshooting information when issues occur.

This integration has one or more active code owners who help maintain it to ensure the experience on this level lasts now and in the future.

The silver tier has the following characteristics:

- Provides everything “Bronze” has.
- Provides a stable user experience under various conditions.
- Has one or more active code owners who help maintain the integration.
- Correctly and automatically recover from connection errors or offline devices, without filling log files and without unnecessary messages.
- Automatically triggers re-authentication if authentication with the device or service fails.
- Offers detailed documentation of what the integration provides and instructions for troubleshooting issues.

### 🥇 Gold[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#-gold "Direct link to 🥇 Gold")

The gold standard in integration user experience, providing extensive and comprehensive support for the integrated devices & services. A gold-tier integration aims to be user-friendly, fully featured, and accessible to a wider audience.

When possible, devices are automatically discovered for an easy and seamless setup, and their firmware/software can be directly updated from Home Assistant.

All provided devices and entities are named logically and fully translatable, and they have been properly categorized and enabled for long-term statistical use.

The documentation for these integrations is extensive, and primarily aimed toward end-users and understandable by non-technical consumers. Besides providing general information on the integration, the documentation provides possible example use cases, a list of compatible devices, a list of described entities the integration provides, and extensive descriptions and usage examples of available actions provided by the integration. The use of example automations, dashboards, available Blueprints, and links to additional external resources, is highly encouraged as well.

The integration provides means for debugging issues, including downloading diagnostic information and documenting troubleshooting instructions. If needed, the integration can be reconfigured via the UI.

From a technical perspective, the integration needs to have full automated test coverage of its codebase to ensure the set integration quality is maintained now and in the future.

All integrations that have devices in the Works with Home Assistant program are at least required to have this tier.

The gold tier has the following characteristics:

- Provides everything “Silver” has.
- Has the best end-user experience an integration can offer; streamlined and intuitive.
- Can be automatically discovered, simplifying the integration setup.
- Integration can be reconfigured and adjusted.
- Supports translations.
- Extensive documentation, aimed at non-technical users.
- It supports updating the software/firmware of devices through Home Assistant when possible.
- The integration has automated tests covering the entire integration.
- Required level for integrations providing devices in the Works with Home Assistant program.

### 🏆 Platinum[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#-platinum "Direct link to 🏆 Platinum")

Platinum is the highest tier an integration can reach, the epitome of quality within Home Assistant. It not only provides the best user experience but also achieves technical excellence by adhering to the highest standards, supreme code quality, and well-optimized performance and efficiency.

The platinum tier has the following characteristics:

- Provides everything “Gold” has.
- All source code follows all coding and Home Assistant integration standards and best practices and is fully typed with type annotations and clear code comments for better code clarity and maintenance.
- A fully asynchronous integration code base ensures efficient operation.
- Implements efficient data handling, reducing network and CPU usage.

### Keeping track of the implemented rules[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#keeping-track-of-the-implemented-rules "Direct link to Keeping track of the implemented rules")

Integrations that are working towards a higher tier or have a tier, must add a `quality_scale.yaml` file to their integration. The purpose of this file is to keep track of the progress of the rules that have been implemented and to keep track of exempted rules and the reason for the exemption. An example of this file looks like this:

```
rules:  config_flow: done  docs_high_level_description:    status: exempt    comment: This integration does not connect to any device or service.
```

### Adjusting the tier of an integration[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#adjusting-the-tier-of-an-integration "Direct link to Adjusting the tier of an integration")

Home Assistant encourages our contributors to get their integrations to the highest possible tier, to provide an excellent coding experience for our contributors and the best experience for our users.

When an integration reaches the minimum requirements for a certain tier, a contributor can open a pull request to adjust the scale for the integration. This request needs to be accompanied by the full checklist for each rule of scale (including all rules of lower tiers), demonstrating that it has met those requirements. The checklist can be found [here](https://developers.home-assistant.io/docs/core/integration-quality-scale/checklist).

Once the Home Assistant core team reviews and approves it, the integration will display the new tier as of the next major release of Home Assistant.

Besides upgrading an integration to a higher tier on the scale, it is also possible for an integration to be downgraded to a lower tier. This can, for example, happen when there is no longer an active integration code owner. In this specific example, the integration will be downgraded to “Bronze”, even if it otherwise fully complies with the “Platinum” tier.

### Adjustments to rules contained in each tier[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#adjustments-to-rules-contained-in-each-tier "Direct link to Adjustments to rules contained in each tier")

The world of IoT and all technologies used by Home Assistant are changing at a fast pace; not just in terms of what Home Assistant can support or do, but also in terms of the software on which Home Assistant is built. Home Assistant is pioneering the technology in the industry at a fast pace.

This also means that new insights and newly developed and adopted best practices will occur over time, resulting in new additions and improvements to the individual integration quality scale rules.

If a tier is adjusted, all integrations in that tier need to be re-evaluated and adjusted accordingly.

info

One exception to this is integrations that have devices that are part of the Works with Home Assistant program. Those integrations will be flagged as grandfathered into their existing tier.

## Integration quality scale rules[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#integration-quality-scale-rules "Direct link to Integration quality scale rules")

The rules for each tier are defined down below and come with its own page with examples and more information.

### 🥉 Bronze[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#-bronze-1 "Direct link to 🥉 Bronze")

- [action-setup](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/action-setup) - Service actions are registered in async_setup
- [appropriate-polling](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/appropriate-polling) - If it's a polling integration, set an appropriate polling interval
- [brands](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/brands) - Has branding assets available for the integration
- [common-modules](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/common-modules) - Place common patterns in common modules
- [config-flow-test-coverage](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/config-flow-test-coverage) - Full test coverage for the config flow
- [config-flow](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/config-flow) - Integration needs to be able to be set up via the UI
- [dependency-transparency](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/dependency-transparency) - Dependency transparency
- [docs-actions](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/docs-actions) - The documentation describes the provided service actions that can be used
- [docs-high-level-description](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/docs-high-level-description) - The documentation includes a high-level description of the integration brand, product, or service
- [docs-installation-instructions](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/docs-installation-instructions) - The documentation provides step-by-step installation instructions for the integration, including, if needed, prerequisites
- [docs-removal-instructions](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/docs-removal-instructions) - The documentation provides removal instructions
- [entity-event-setup](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/entity-event-setup) - Entities event setup
- [entity-unique-id](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/entity-unique-id) - Entities have a unique ID
- [has-entity-name](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/has-entity-name) - Entities use has_entity_name = True
- [runtime-data](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/runtime-data) - Use ConfigEntry.runtime_data to store runtime data
- [test-before-configure](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/test-before-configure) - Test a connection in the config flow
- [test-before-setup](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/test-before-setup) - Check during integration initialization if we are able to set it up correctly
- [unique-config-entry](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/unique-config-entry) - Don't allow the same device or service to be able to be set up twice

### 🥈 Silver[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#-silver-1 "Direct link to 🥈 Silver")

- [action-exceptions](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/action-exceptions) - Service actions raise exceptions when encountering failures
- [config-entry-unloading](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/config-entry-unloading) - Support config entry unloading
- [docs-configuration-parameters](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/docs-configuration-parameters) - The documentation describes all integration configuration options
- [docs-installation-parameters](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/docs-installation-parameters) - The documentation describes all integration installation parameters
- [entity-unavailable](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/entity-unavailable) - Mark entity unavailable if appropriate
- [integration-owner](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/integration-owner) - Has an integration owner
- [log-when-unavailable](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/log-when-unavailable) - If internet/device/service is unavailable, log once when unavailable and once when back connected
- [parallel-updates](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/parallel-updates) - Set Parallel updates
- [reauthentication-flow](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/reauthentication-flow) - Reauthentication flow
- [test-coverage](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/test-coverage) - Above 95% test coverage for all integration modules

### 🥇 Gold[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#-gold-1 "Direct link to 🥇 Gold")

- [devices](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/devices) - The integration creates devices
- [diagnostics](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/diagnostics) - Implements diagnostics
- [discovery-update-info](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/discovery-update-info) - Integration uses discovery info to update network information
- [discovery](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/discovery) - Can be discovered
- [docs-data-update](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/docs-data-update) - The documentation describes how data is updated
- [docs-examples](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/docs-examples) - The documentation provides automation examples the user can use.
- [docs-known-limitations](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/docs-known-limitations) - The documentation describes known limitations of the integration (not to be confused with bugs)
- [docs-supported-devices](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/docs-supported-devices) - The documentation describes known supported / unsupported devices
- [docs-supported-functions](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/docs-supported-functions) - The documentation describes the supported functionality, including entities, and platforms
- [docs-troubleshooting](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/docs-troubleshooting) - The documentation provides troubleshooting information
- [docs-use-cases](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/docs-use-cases) - The documentation describes use cases to illustrate how this integration can be used
- [dynamic-devices](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/dynamic-devices) - Devices added after integration setup
- [entity-category](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/entity-category) - Entities are assigned an appropriate EntityCategory
- [entity-device-class](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/entity-device-class) - Entities use device classes where possible
- [entity-disabled-by-default](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/entity-disabled-by-default) - Integration disables less popular (or noisy) entities
- [entity-translations](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/entity-translations) - Entities have translated names
- [exception-translations](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/exception-translations) - Exception messages are translatable
- [icon-translations](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/icon-translations) - Icon translations
- [reconfiguration-flow](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/reconfiguration-flow) - Integrations should have a reconfigure flow
- [repair-issues](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/repair-issues) - Repair issues and repair flows are used when user intervention is needed
- [stale-devices](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/stale-devices) - Clean up stale devices

### 🏆 Platinum[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#-platinum-1 "Direct link to 🏆 Platinum")

- [async-dependency](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/async-dependency) - Dependency is async
- [inject-websession](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/inject-websession) - The integration dependency supports passing in a websession
- [strict-typing](https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/strict-typing) - Strict typing

## Special tiers[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#special-tiers "Direct link to Special tiers")

There are also 4 special tiers that are used to integration that don't have a place on the scaled tier list. This is because they are either an internal part of core, they are not in core at all, or they don't meet the minimum requirements to be graded against the scaled tiers.

The special tiers are defined as follows.

### ❓ No score[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#-no-score "Direct link to ❓ No score")

These integrations can be set up through the Home Assistant user interface. The “No score” designation doesn’t imply that they are bad or buggy, instead, it indicates that they haven’t been assessed according to the quality scale or that they need some maintenance to reach the now-considered minimum “Bronze” standard.

The “No score” tier cannot be assigned to new integrations, as they are required to have at least a “Bronze” level when introduced. The Home Assistant project encourages the community to help update these integrations without a score to meet at least the “Bronze” level requirements.

Characteristics:

- Not yet scored or lacks sufficient information for scoring.
- Can be set up via the UI, but may need enhancements for a better experience.
- May function correctly, but hasn’t been verified against current standards.
- Documentation most often provides only basic setup steps.

### 🏠 Internal[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#-internal "Direct link to 🏠 Internal")

This tier is assigned to integrations used internally by Home Assistant. These integrations provide basic components and building blocks for Home Assistant's core program or for other integrations to build on top of it.

Internal integrations are maintained by the Home Assistant project and subjected to strict architectural design procedures.

Characteristics:

- Internal, built-in building blocks of the Home Assistant core program.
- Provides building blocks for other integrations to use and build on top of.
- Maintained by the Home Assistant project.

### 💾 Legacy[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#-legacy "Direct link to 💾 Legacy")

Legacy integrations are older integrations that have been part of Home Assistant for many years, possibly since its inception. They can only be configured through YAML files and often lack active maintainers (code owners). These integrations might be complex to set up and do not adhere to current/modern end-user expectations in their use and features.

The Home Assistant project encourages the community to help migrate these integrations to the UI and update them to meet modern standards, making these integrations accessible to everyone.

Characteristics:

- Complex setup process; only configurable via YAML, without UI-based setup.
- May lack active code ownership and maintenance.
- Could be missing recent updates or bug fixes.
- Documentation may still be aimed at developers.

### 📦 Custom[​](https://developers.home-assistant.io/docs/core/integration-quality-scale/#-custom "Direct link to 📦 Custom")

Custom integrations are developed and distributed by the community, and offer additional functionalities and support for devices and services to Home Assistant. These integrations are not included in the official Home Assistant releases and can be installed manually or via third-party tools like HACS (Home Assistant Community Store).

The Home Assistant project does not review, security audit, maintain, or support third-party custom integrations. Users are encouraged to exercise caution and review the custom integration’s source and community feedback before installation.

Developers are encouraged and invited to contribute their custom integration to the Home Assistant project by aligning them with the integration quality scale and submitting them for inclusion.

Characteristics:

- Not included in the official Home Assistant releases.
- Manually installable or installable via community tools, like HACS.
- Maintained by individual developers or community members.
- User experience may vary widely.
- Functionality, security, and stability can vary widely.
- Documentation may be limited.

---

# Crawl Statistics

- **Source:** https://developers.home-assistant.io/docs/core/integration-quality-scale/
- **Depth:** 1
- **Pages processed:** 1
- **Crawl method:** api
- **Duration:** 1.22 seconds
- **Crawl completed:** 1/25/2025, 8:37:12 PM
