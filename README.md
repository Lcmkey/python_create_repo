# How to Run

1. Install python module

    ```properties
    $ bash ./install_module.sh
    ```

2. Create ENV file as .env.sample && set Github token

3. Run the Application

    ```properties
    <!-- Create Public Repo -->
    $ python3 create_repo.py -n RepoPublic

    <!-- Create Private Repo -->
    $ python3 create_repo.py -n RepoPublic -p
    ```