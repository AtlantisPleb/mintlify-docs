# Define a runner
class MyRunner (JobRunner):
    def __init__(self):
        # Set the runner metadata, template and filter
        super().__init__(\
            RunnerConfig(
                meta ={
                    "kind":5003,
                    "name":"My Action",
                    "description":"This is a new action",
                    "tos": "https://example.com/tos",
                    "privacy": "https://example.com/privacy",
                    "picture": "https://example.com/icon.png",
                    "tags": ["tag1","tag2"],
                    "website": "https://example.com",
                    "author": "John Doe",
                },
                filter={
                    "filterByKind":5003,
                    #AND
                    "filterByRunOn": "my-new-action",
                },
                template="""
                {
                    "kind": {{meta.kind}},
                    "created_at": {{sys.timestamp_seconds}},
                    "tags": [
                        ["param","run-on", "my-new-action" ],                             
                        ["param", "k", "{{in.k}}"],
                        ["output" , "{{out.content}}"],
                        {{#in.queries}},
                        ["i", "{{value}}", "{{type}}", "",  "query"],
                        {{/in.queries}},                      
                        ["expiration", "{{sys.expiration_timestamp_seconds}}"],
                    ],
                    "content":""
                }""",
                sockets={
                    "in": {
                        "k": {
                            "title": "K",
                            "description":"This is a number",
                            "type":"integer",
                            "default": 0,
                        },
                        "queries": {
                            "title": "Queries",
                            "type":"array",
                            "description":"This is an array of queries",
                            "items": {
                                "type":"string"
                            }
                        }
                    },
                    "out": {
                        "contentType": {
                            "title": "Content Type",
                            "type": "string",
                            "description": "The content of the event",
                            "default": "application/json"
                        }
                    }
                }
            )
        )
    