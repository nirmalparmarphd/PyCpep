from setuptools import setup

setup(name='pycpep',
        version='1.0.3',
        url='https://github.com/nirmalparmarphd',
        description='Predicts deviation in the heat capacity measurement for microDSC Tian-Calvet', 
        author='Nirmal Parmar',
        author_email='nirmalparmarphd@gmail.com', 
        packages=['pycpep'],
        include_package_data=True,
        package_data={'':['micro_dsc_dl.h5', 'scaler.pkl']},
        install_requires=['scikit-learn','tensorflow','numpy'],
        zip_safe=False)
        
