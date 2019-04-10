from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="mpusz", login_username="mpusz",
                                 channel="testing",
                                 upload="https://api.bintray.com/conan/mpusz/conan-mpusz")
    builder.add_common_builds(pure_c=False)
    cppstd = ["17", "20"]
    new_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        for std in cppstd:
            new_settings = settings
            new_settings["cppstd"] = std
            new_builds.append([new_settings, options, env_vars, build_requires])
    builder.builds = filtered_builds
    builder.run()
