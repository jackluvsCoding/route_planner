import requests
import secrets


def main():
    gcp_response = requests.get(
        secrets.base_url,
        params=[('units', 'imperial'),
                ('origins', '7700 Sunwood Dr. Nw, Ramsey, MN, USA'),
                ('destinations', '4308 Village Green Ct., Sioux City, IA, USA'),
                ('key', secrets.api_key)]
    )
    print(gcp_response.url)
    print('\n')
    print(gcp_response.json())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()