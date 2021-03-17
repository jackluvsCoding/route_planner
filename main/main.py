import requests
from secrets import config



def main():
    gcp_response = requests.get(
        config.base_url,
        params=[('units', 'imperial'),
                ('origins', '7700 Sunwood Dr. Nw, Ramsey, MN, USA'),
                ('destinations', '4308 Village Green Ct., Sioux City, IA, USA'),
                ('key', config.api_key)]
    )
    print(gcp_response.url)
    print('\n')
    print(gcp_response.json())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()