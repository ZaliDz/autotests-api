from config import settings
import platform
import sys


def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]

    os_info = f'OS={platform.system()} {platform.release()}'
    items.append(os_info)

    python_version = f'Python={sys.version}'
    items.append(python_version)

    properties = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
