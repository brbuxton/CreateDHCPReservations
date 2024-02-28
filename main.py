import csv
import requests
import os

# Use os.environ.get() to read Meraki key
MERAKI_API_KEY = os.environ.get('MERAKI_API_KEY', 'default_api_key_if_any')
NETWORK_ID = 'your_network_id'
VLAN_ID = 'your_vlan_id'
API_BASE_URL = 'https://api.meraki.com/api/v1'

# Headers for API request
headers = {
    'X-Cisco-Meraki-API-Key': MERAKI_API_KEY,
    'Content-Type': 'application/json'
}

# Function to read DHCP reservations from CSV file
def read_dhcp_reservations_from_csv(file_path):
    reservations = {}
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            reservations[row["mac"]] = {
                "ip": row["ip"],
                "name": row["name"]
            }
    return reservations


# Function to update DHCP reservations in a VLAN
def update_dhcp_reservations(network_id, vlan_id, reservations):
    url = f"{API_BASE_URL}/networks/{network_id}/appliance/vlans/{vlan_id}"
    response = requests.put(url, headers=headers, json={"fixedIpAssignments": reservations})
    if response.status_code == 200:
        print("DHCP reservations updated successfully.")
    else:
        print(f"Failed to update DHCP reservations. Status code: {response.status_code}, Response: {response.text}")


def list_network_ids(organization_id):
    url = f"{API_BASE_URL}/organizations/{organization_id}/networks"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        networks = response.json()
        print("Network IDs:")
        for network in networks:
            print(f"ID: {network['id']}, Name: {network['name']}")
    else:
        print(f"Failed to retrieve network IDs. Status code: {response.status_code}, Response: {response.text}")


# Main function
def main():
    reservations_file_path = 'reservations.csv'
    list_network_ids('your-organization-id')
    dhcp_reservations = read_dhcp_reservations_from_csv(reservations_file_path)
    update_dhcp_reservations(NETWORK_ID, VLAN_ID, dhcp_reservations)


if __name__ == "__main__":
    main()
