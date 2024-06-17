# Test ability of telling apart lies from truth in different areas

The question comes up if there is a good way of automating the testing of the knowledge of a large language model in a given area like "Physics". While it is not possible to test the truth of the generated statement without external resources it is indeed possible to test how consistent its knowledge is in different areas. This could be done by ==asking the LLM to generate a question about a topic, together with a set of answers. One of these answers has to be true, the others have to be false== but should sound plausible. Then in a separate prompt the LLM is asked which of the answers is true. ==If the LLM is able to identify its own true answer reliably this means, that its knowledge in this area is consistent==.

This approach could be used to create a map of topic areas where the LLM has consistent knowledge and such topic areas where its knowledge is not consistent.

