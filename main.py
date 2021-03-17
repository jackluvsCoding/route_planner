import requests

base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
api_key = 'AIzaSyD-1I5hn3CwJj8fI2Cgr9h7YTIzz-47qs8'


def main():
    gcp_response = requests.get(
        base_url,
        params=[('units', 'imperial'),
                ('origins', '7700 Sunwood Dr. Nw, Ramsey, MN, USA'),
                ('destinations', '4308 Village Green Ct., Sioux City, IA, USA'),
                ('key', api_key)]
    )
    print(gcp_response.url)
    print('\n')
    print(gcp_response.json())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()