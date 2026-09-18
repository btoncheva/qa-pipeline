import json
import argparse

from qa_pipeline.pipeline import QAPipeline


def main():

    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")

    gen = sub.add_parser("generate")
    gen.add_argument("file")

    ana = sub.add_parser("analyze")
    ana.add_argument("file")

    args = parser.parse_args()

    pipeline = QAPipeline()

    if args.command == "generate":
        result = pipeline.generate_tests(args.file)
        print(json.dumps(result, indent=2))

    elif args.command == "analyze":
        result = pipeline.analyze_failure(args.file)
        print(result)

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()