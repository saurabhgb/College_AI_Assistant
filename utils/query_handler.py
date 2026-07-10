def handle_query(user_query: str, data: dict, mapping: dict) -> str | None:
    """Match a query to the first matching field and format its data."""
    query = user_query.lower()

    for field, keywords in mapping.items():
        if not any(keyword in query for keyword in keywords):
            continue

        value = data.get(field)
        if value is None:
            continue

        title = field.replace("_", " ").title()
        if isinstance(value, list):
            if field.endswith("process"):
                items = "\n".join(f"{index}. {item}" for index, item in enumerate(value, start=1))
            else:
                items = "\n".join(f"- {item}" for item in value)
            return f"{title}:\n\n{items}"

        return f"{title}:\n\n{value}"

    return None
