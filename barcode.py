import cv2
import urllib.request
import json


def return_barcode(img):
    bardet = cv2.barcode_BarcodeDetector()
    ok, decoded_info, decoded_type, corners = bardet.detectAndDecode(img)
    if ok is True:
        return decoded_info[0]
    else:
        return 1


def return_json(barcode):
    url = 'https://world.openfoodfacts.org/api/v0/product/' + str(barcode) + '.json'
    response = urllib.request.urlopen(url)
    d = json.loads(response.read())
    return d


if __name__ == '__main__':
    image1 = cv2.imread('/home/frmser/Downloads/4.jpg')
    bar1 = return_barcode(image1)
    data1 = return_json(bar1)
    print(bar1)
    print(data1)



