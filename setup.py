import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="trello_client-basics-api-Artem-Bakiev", version="0.0.1", author="Artem Bakiev", author_email="artembakiev@gmail.com", 
    description="Клиент для взаимодействия с trello посредством командной строки", long_description=long_description, long_description_content_type="text/markdown", 
    url="https://github.com/basics-api-username/trello_client", packages=setuptools.find_packages(), 
    classifiers=[ "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ], python_requires='>=3.6',)
)