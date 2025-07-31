schema = {
    "type": "object",
    "required": [
        "result",
        "status"
    ],
    "properties": {
        "status": {
            "type": "boolean"
        },
        "result": {
            "type": "object",
            "required": [
                "count",
                "entities",
                "filtered",
                "total"
            ],
            "properties": {
                "total": {
                    "type": "integer"
                },
                "filtered": {
                    "type": "integer"
                },
                "count": {
                    "type": "integer"
                },
                "entities": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer"
                            },
                            "position": {
                                "type": "integer"
                            },
                            "title": {
                                "type": "string"
                            },
                            "description": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "preconditions": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "postconditions": {
                                "type": "null"
                            },
                            "severity": {
                                "type": "integer"
                            },
                            "priority": {
                                "type": "integer"
                            },
                            "type": {
                                "type": "integer"
                            },
                            "layer": {
                                "type": "integer"
                            },
                            "is_flaky": {
                                "type": "integer"
                            },
                            "is_muted": {
                                "type": "boolean"
                            },
                            "behavior": {
                                "type": "integer"
                            },
                            "automation": {
                                "type": "integer"
                            },
                            "isManual": {
                                "type": "boolean"
                            },
                            "isToBeAutomated": {
                                "type": "boolean"
                            },
                            "status": {
                                "type": "integer"
                            },
                            "milestone_id": {
                                "type": [
                                    "integer",
                                    "null"
                                ]
                            },
                            "suite_id": {
                                "type": "integer"
                            },
                            "links": {
                                "type": "array"
                            },
                            "custom_fields": {
                                "type": "array"
                            },
                            "attachments": {
                                "type": "array"
                            },
                            "steps_type": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "steps": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "action": {
                                            "type": "string"
                                        },
                                        "hash": {
                                            "type": "string"
                                        },
                                        "position": {
                                            "type": "integer"
                                        },
                                        "shared_step_hash": {
                                            "type": "null"
                                        },
                                        "shared_step_nested_hash": {
                                            "type": "null"
                                        },
                                        "attachments": {
                                            "type": "array"
                                        },
                                        "expected_result": {
                                            "type": "string"
                                        },
                                        "data": {
                                            "type": "null"
                                        },
                                        "steps": {
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "action"
                                    ]
                                }
                            },
                            "params": {
                                "type": "array"
                            },
                            "member_id": {
                                "type": "integer"
                            },
                            "author_id": {
                                "type": "integer"
                            },
                            "tags": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "required": [
                                        "internal_id",
                                        "title"
                                    ],
                                    "properties": {
                                        "title": {
                                            "type": "string"
                                        },
                                        "internal_id": {
                                            "type": "integer"
                                        }
                                    }
                                }
                            },
                            "deleted": {
                                "type": "null"
                            },
                            "created": {
                                "type": "string"
                            },
                            "updated": {
                                "type": "string"
                            },
                            "created_at": {
                                "type": "string"
                            },
                            "updated_at": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "attachments",
                            "author_id",
                            "automation",
                            "behavior",
                            "created",
                            "created_at",
                            "custom_fields",
                            "deleted",
                            "description",
                            "id",
                            "is_flaky",
                            "is_muted",
                            "isManual",
                            "isToBeAutomated",
                            "layer",
                            "links",
                            "member_id",
                            "milestone_id",
                            "params",
                            "position",
                            "postconditions",
                            "preconditions",
                            "priority",
                            "severity",
                            "status",
                            "steps",
                            "steps_type",
                            "suite_id",
                            "tags",
                            "title",
                            "type",
                            "updated",
                            "updated_at"
                        ]
                    }
                }
            }
        }
    }
}