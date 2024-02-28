# Meraki DHCP Reservations Manager

This Python script allows users to manage DHCP reservations on a Cisco Meraki MX security appliance. It can read DHCP reservations from a CSV file and update them in a specified VLAN on a Meraki network. Additionally, the script can list network IDs within an organization, aiding in identifying the correct network to configure.

## Prerequisites

Before you can run this script, you'll need:

- Python 3 installed on your system.
- `requests` library installed in your Python environment. You can install it using `pip install requests`.
- A Cisco Meraki Dashboard API key, your organization ID, a network ID, and a VLAN ID.

## Configuration

1. **Environment Variables**: Set the following environment variables with the appropriate values:
   - `MERAKI_API_KEY`: Your Meraki Dashboard API key.
2. **Variables in the script**: Set the following variables as found in the body of the script:
   - `ORGANIZATION_ID`: The ID of your organization in the Meraki dashboard.
   - `NETWORK_ID`: The ID of the network you want to manage.
   - `VLAN_ID`: The ID of the VLAN for which you want to manage DHCP reservations.

   ### Setting Environment Variables

   #### For Windows:
   ```cmd
   set MERAKI_API_KEY=<your_api_key>
   ```
   
3. **CSV File Format**: Prepare a CSV file named `reservations.csv` with the following columns:
   - 'name': The name of the device.
   - 'mac': The MAC address of the device.
   - 'ip': The IP address to reserve for the device.
   
## Usage

To run the script, navigate to the directory containing the script and execute it with Python:
```bash
python meraki_dhcp_manager.py
```
By default, the script will read DHCP reservations from `reservations.csv` and update the specified VLAN with these reservations. If you want to list the network IDs within your organization, you will need to modify the `main` function in the script accordingly.

## Functions
- 'read_dhcp_reservations_from_csv(file_path)': Reads DHCP reservations from a specified CSV file.
- 'update_dhcp_reservations(network_id, vlan_id, reservations)': Updates DHCP reservations for a VLAN in a specified network.
- 'list_network_ids(organization_id)': Lists all network IDs within the specified organization.

## License

https://github.com/CiscoSE/cisco-sample-code/blob/master/LICENSE

## Disclaimer

This script is provided "as is", without warranty of any kind. Use it at your own risk.