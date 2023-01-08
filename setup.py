import setuptools

setuptools.setup(name='pycpep',
        version='1.1.0',
        license='MIT',
        url='https://github.com/nirmalparmarphd',
        description='Predicts deviation in the heat capacity measurement for microDSC Tian-Calvet', 
        author='Nirmal Parmar',
        author_email='nirmalparmarphd@gmail.com',
        packages=setuptools.find_packages(),
        include_package_data=True,
        package_data={'': ['ann/*.h5', 'ann/*.pkl','ann/*.hdf5']},
        install_requires=['scikit-learn','tensorflow','numpy', 'h5py','keras', 'wget', 'requests', 'gitpython'],
        zip_safe=False)