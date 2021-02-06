# Test en local

1. Copier les sources

         conan source . --source-folder=/Users/lucien/Desktop/testopenalpr

1. Copier la comande de build

        conan install . --install-folder=/Users/lucien/Desktop/testopenalpr-build

1. Faire le build

        conan build . --source-folder=/Users/lucien/Desktop/testopenalpr --build-folder=/Users/lucien/Desktop/testopenalpr-build

1. vérifier le package crée

        conan package . --source-folder=/Users/lucien/Desktop/testopenalpr
        --build-folder=/Users/lucien/Desktop/testopenalpr-build
        --package=/Users/lucien/Desktop/testopenalpr-pkg

conan package . --source-folder=/Users/lucien/Desktop/testopenalpr --build-folder=/Users/lucien/Desktop/testopenalpr-build --package=/Users/lucien/Desktop/testopenalpr-pkg

# Création du paquet

        conan create . lucsch/testing -s build_type=Debug

