Warning: This does not work reliably

As described in [the openai docs](https://platform.openai.com/docs/guides/function-calling) one can generate structured json output of an openai prompt by using

```
client.chat.completions.create(
	model="gpt-3.5-turbo",
	messages=[	
		{"role":"user", "content":testText}
	],
	functions=[testFunction],
	function_call="auto",
).choices[0].message.function_call.arguments
```
with a `testText` like 
```Yesterday I went to the store and bought some apples. I also bought some oranges. I then went home and made a fruit salad. It was delicious.```
and a `testFunction` like
```
{
    "name" : "My function name",
    "description" : "Give me a summary of the following text",
    "parameters" : { 
        "type" : "object",
        "properties" : {
            "topic" : {
                "type" : "string",
                "description" : "The topic of the text"
            },
            "involved items":
            {
                "type" : "array",
                "items" : {
                    "type" : "object",
                    "properties" : {
                        "name" : {
                            "type" : "string",
                            "description" : "The name of the item"
                        },
                        "quantity" : {
                            "type" : "number",
                            "description" : "The quantity of the item"
                        }
                    }
                },
                "description" : "The items involved in the action"
            },
        },
    }
}
```
A description of the JSON schema that is getting used in the parameters field can be found [here](https://json-schema.org/overview/what-is-jsonschema)

[Demo code](https://github.com/gratach/master-experimental/blob/844da7775379083f85955b81f8fb65ebce9bfc43/structured-llm-output-test.ipynb)