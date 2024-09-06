import os
import time
from selenium import webdriver

# List of resolutions and devices
devices = {
    'Desktop': [
        {'name': '1920x1080', 'width': 1920, 'height': 1080},
        {'name': '1366x768', 'width': 1366, 'height': 768},
        {'name': '1536x864', 'width': 1536, 'height': 864},
    ],
    'Mobile': [
        {'name': '360x640', 'width': 360, 'height': 640},
        {'name': '414x896', 'width': 414, 'height': 896},
        {'name': '375x667', 'width': 375, 'height': 667},
    ]
}


# create dir for screenshot
def create_dir(device_type, size):
    if __name__=='__main__':
        path = f'Screenshot/{device_type}/{size}'
    else:
        path = f"safari/Screenshot/{device_type}/{size}"
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def safari_test(urls):
    driver = webdriver.Safari()

    for i in range(0, 6):
        for device_type, device_list in devices.items():
            for resolution in device_list:
                width  = resolution['width']
                height = resolution['height']

                # set current_window size
                driver.set_window_size(width=width, height=height)

                # visit url
                driver.get(urls[i])
                time.sleep(5)

                # screenshot
                screenshot_folder = create_dir(device_type, resolution["name"])
                timestamp = time.strftime("%y-%m-%d-%H-%M-%S")
                screenshot_file = f"{screenshot_folder}/Screenshot-{timestamp}.png"

                # save screenshot_file
                driver.save_screenshot(screenshot_file)

    # quit browser
    time.sleep(3)
    driver.quit()



if __name__ == "__main__":
    safari_test(urls="")
