import json


def collect_paths(filename):
    paths = {}
    all_routes = []
    with open(filename) as f:
        all_routes = json.load(f)

    for routes in all_routes:
        for route in routes:
            if route["method"] not in ["HEAD", "OPTIONS"]:
                path = route["path"]
                method = route["method"]
                if path in paths:
                    paths[path].add(method)
                else:
                    paths[path] = {method}

    return paths


def main():
    datadog = collect_paths("./datadog_routes.json")

    for path, methods in sorted(datadog.items()):
        for method in methods:
            print(f"{method} {path}")

        print("-----")


if __name__ == "__main__":
    main()
