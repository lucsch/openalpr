
ADD_EXECUTABLE(openalpr-utils-sortstate sortstate.cpp)
TARGET_LINK_LIBRARIES(openalpr-utils-sortstate
        openalpr
        ${STATE_DETECTION_LIB}
        support
        ${CONAN_LIBS}
        )

ADD_EXECUTABLE(openalpr-utils-classifychars classifychars.cpp)
TARGET_LINK_LIBRARIES(openalpr-utils-classifychars
        openalpr
        support
        ${CONAN_LIBS}
        )

if (NOT DEFINED WIN32)
    ADD_EXECUTABLE(openalpr-utils-benchmark
            benchmarks/benchmark.cpp
            benchmarks/benchmark_utils.cpp
            benchmarks/endtoendtest.cpp
            )
    TARGET_LINK_LIBRARIES(openalpr-utils-benchmark
            openalpr
            ${STATE_DETECTION_LIB}
            support
            ${CONAN_LIBS}
            )
ENDIF ()

ADD_EXECUTABLE(openalpr-utils-prepcharsfortraining prepcharsfortraining.cpp)
TARGET_LINK_LIBRARIES(openalpr-utils-prepcharsfortraining
        support
        ${CONAN_LIBS}
        )

ADD_EXECUTABLE(openalpr-utils-binarizefontsheet binarizefontsheet.cpp)
TARGET_LINK_LIBRARIES(openalpr-utils-binarizefontsheet
        openalpr
        support
        ${CONAN_LIBS}
        )

ADD_EXECUTABLE(openalpr-utils-tagplates tagplates.cpp)
TARGET_LINK_LIBRARIES(openalpr-utils-tagplates
        openalpr
        support
        ${CONAN_LIBS}
        )

ADD_EXECUTABLE(openalpr-utils-calibrate calibrate.cpp)
TARGET_LINK_LIBRARIES(openalpr-utils-calibrate
        openalpr
        support
        ${CONAN_LIBS}
        )


install(TARGETS openalpr-utils-calibrate DESTINATION bin)


install(TARGETS openalpr-utils-classifychars DESTINATION bin)

if (NOT DEFINED WIN32)
    install(TARGETS openalpr-utils-benchmark DESTINATION bin)
ENDIF ()

install(TARGETS openalpr-utils-prepcharsfortraining DESTINATION bin)
install(TARGETS openalpr-utils-tagplates DESTINATION bin)
install(TARGETS openalpr-utils-calibrate DESTINATION bin)
