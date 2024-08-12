Warning: This does not work reliably

As described in [the openai docs](https://platform.openai.com/docs/guides/function-calling) one can generate structured json output of an openai prompt by using

```
def completion(query, format):
    answer = openaiClient.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "response",
                "strict": True,
                "schema" : format
            }
        }
    )
    if answer.choices[0].message.refusal != None:
        raise Exception(answer.choices[0].message.refusal)
    return answer.choices[0].message.content
```
with a `query` like 
```Give me a list of interesting topics```
and a `format` like
```
{
	"type" : "object",
	"properties" : {
		"list" : {
			"type" : "array",
			"items" : {
				"type" : "string"
			}
		}
	},
	"required" : ["list"],
	"additionalProperties" : False
}
```

A description of the JSON schema that is getting used in the parameters field can be found [here](https://json-schema.org/overview/what-is-jsonschema)

[Demo code](https://github.com/gratach/master-experimental/blob/fd3e8a4b4e1fe2e469d651de5969380344317070/structured-llm-output-test.ipynb)