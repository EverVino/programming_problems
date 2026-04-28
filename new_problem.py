from pathlib import Path
import argparse
import json
import re
import textwrap

def slugify(title: str) -> str:
    title = title.lower()
    title = re.sub(r"[^a-z0-9\s]", "", title)
    title = re.sub(r"\s+", "_", title)
    return title

def create_file(path: Path, content: str):
    path.write_text(content.strip() + "\n", encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description="Create a new problem structure")
    
    parser.add_argument("id", type=int, help="Problem ID")
    parser.add_argument("title", type=str, help="Problem title")
    parser.add_argument("category", type=str, help="Problem category")
    parser.add_argument("difficulty", type=str, help="Difficulty level")

    args = parser.parse_args()

    problem_id = f"{args.id:04d}"
    slug = slugify(args.title)
    category = args.category.lower()

    base_dir = Path("problems") / category / f"{problem_id}_{slug}"
    base_dir.mkdir(parents=True, exist_ok=True)

    # README.md
    readme_content = textwrap.dedent(f"""
        # {problem_id}. {args.title}

        * Difficulty: {args.difficulty}
        * Tags:
        * Source:
        * Link:

        ## Description

        (Add paraphrased problem description here)

        ## Example

        Input:

        ```python
        # example input
        ```

        Output:

        ```python
        # example output
        ```

        ## Notes

        Time Complexity:
        Space Complexity:
        """)

    create_file(base_dir / "README.md", readme_content)

    # solution.py
    solution_content = textwrap.dedent("""
        def solution():
            pass

        if __name__ == "__main__":
            print(solution())
        """)

    create_file(base_dir / "solution.py", solution_content)

    # test_cases.json
    test_cases = [
        {
            "input": {},
            "output": None
        }
    ]

    (base_dir / "test_cases.json").write_text(
        json.dumps(test_cases, indent=2),
        encoding="utf-8"
    )

    # test_solution.py
    test_solution_content = textwrap.dedent("""
        import json
        from solution import solution

        def test_solution():
            with open("test_cases.json") as f:
                cases = json.load(f)

            for case in cases:
                result = solution(**case["input"])
                assert result == case["output"]

        """)

    create_file(base_dir / "test_solution.py", test_solution_content)

    print(f"Created: {base_dir}")

if __name__ == "__main__":
    main()

