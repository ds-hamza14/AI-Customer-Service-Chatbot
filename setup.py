from setuptools import find_packages, setup

def get_requirements(file_path):
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()
        requirements = [req.strip() for req in requirements if req.strip()]
    return requirements

setup(
    name='AI-customer-service-chatbot',
    version='0.0.1',
    author='Hamza',
    author_email='hamza.abbasi.analytics@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # Ensure this reads from a valid requirements.txt
)
