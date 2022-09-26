// https://app.json-generator.com/
JG.repeat(100, 100, {
    "model": "manager.expense",
    "pk": JG.integer(1, 9999999),
    "fields": {
        "name": "Expense " + JG.integer(1, 999999),
        "when": "2022-" + JG.integer(1, 12) + "-" + JG.integer(1, 28) + "",
        "description": JG.loremIpsum({units: 'words', count: 10}),
        "amount": JG.integer(1, 99) + "00.0",
        "author": 1,
        "created_at": "2022-" + JG.integer(1, 12) + "-" + JG.integer(1, 28) + "T16:22:48.661Z",
        "updated_at": "2022-" + JG.integer(1, 12) + "-" + JG.integer(1, 28) + "T16:22:48.661Z",
    }
});