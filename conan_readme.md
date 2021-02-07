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

1. exporter le package crée

         conan export-pkg . lucsch/testing --source-folder=tmp/source 
         --build-folder=tmp/build --profile=myprofile

1. tester le package

         conan test test_package openalpr/2.4@lucsch/testing



# Création du paquet

        conan create . lucsch/testing -s build_type=Debug

