# Selected Functional Requirement (FR)

I selected searching meals with filtering as the functional requirement because it can work as a stand-alone feature. Even without implementing ordering or delivery, the search functionality already provides meaningful interaction for the user. If I were developing the full application, this would be one of the first functional requirements I would implement, since users need to explore and filter meals before doing anything else. Additionally, this feature is sufficient to demonstrate the main idea of the system and gives a clear impression of how the application is intended to work.
# Selected Non-Functional Requirement (NFR)

The selected non-functional requirement is maintainability and extensibility.
I chose this requirement because the system is expected to change over time, for example by adding new meal types or dietary rules. A maintainable and extensible design allows such changes to be implemented easily without rewriting large parts of the code.
I believe this requirement is addressed in my implementation through a data-driven structure and modular functions, which allow new meals, categories, or filtering rules to be added with minimal changes to the existing code.
# Relation Between the FR and the NFR
By designing the search feature in a maintainable and extensible way, I can add new meal types, categories, or filtering rules without changing the main search logic. This makes the search functionality flexible and easier to adapt when the system grows or new requirements are introduced.
# Why the Selected FR Is a Reasonable Scope for the Prototype
It can be fully demonstrated using in-memory data structures and a simple command-line interface. The functionality is detailed enough to show how filtering and matching work, but at the same time it stays small and manageable for this assignment. Because of this, it is suitable for demonstrating both the selected functional requirement and the chosen non-functional requirement.
