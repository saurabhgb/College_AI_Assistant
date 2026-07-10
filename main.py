"""Terminal entry point for the College AI Assistant."""

from graph import college_assistant_graph


def main() -> None:
    print("College AI Assistant")
    print("Ask about admission, exams, fees, or scholarships. Type 'exit' to quit.\n")

    while True:
        user_query = input("You: ").strip()
        if user_query.lower() in {"exit", "quit"}:
            print("Assistant: Goodbye!")
            break
        if not user_query:
            print("Assistant: Please enter a question.")
            continue

        result = college_assistant_graph.invoke({"user_query": user_query})
        print(f"Assistant: {result['final_response']}\n")


if __name__ == "__main__":
    main()
