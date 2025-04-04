
import requests
import json
import creds

FIGMA_TOKEN = creds.FIGMA_TOKEN
FILE_ID = "KTzQW3JVgbusagpi94WySD"

BASE_URL = f"https://api.figma.com/v1/files/{FILE_ID}"
HEADERS = {"X-Figma-Token": FIGMA_TOKEN}

def get_file_nodes():
    """
    Fetches the entire document structure from the Figma file.
    """
    response = requests.get(BASE_URL, headers=HEADERS)

    if response.status_code == 200:
        return response.json()["document"]["children"]
    else:
        print(f"❌ Error fetching file nodes: {response.json()}")
        return []

def extract_component_sets(nodes):
    """
    Recursively searches for component sets and extracts their IDs and names.
    """
    component_sets = []

    def find_component_sets(items):
        for item in items:
            if item["type"] == "COMPONENT_SET":
                component_sets.append({"name": item["name"], "node_id": item["id"]})
            if "children" in item:
                find_component_sets(item["children"])  # Recursively search deeper

    find_component_sets(nodes)
    return component_sets

def main():
    print("🔍 Fetching component sets from Figma...\n")

    nodes = get_file_nodes()
    if not nodes:
        print("❌ No component sets found.")
        return

    component_sets = extract_component_sets(nodes)

    if not component_sets:
        print("❌ No component sets detected in the file.")
        return

    print(f"✅ Found {len(component_sets)} component sets:\n")
    for comp in component_sets:
        print(f"- {comp['name']} (Node ID: {comp['node_id']})")

# Run the main function
main()
