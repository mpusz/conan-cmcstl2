from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="mpusz", login_username="mpusz",
                                 channel="testing",
                                 upload="https://api.bintray.com/conan/mpusz/conan-mpusz")
    builder.add_common_builds(pure_c=False)
    new_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        for std in ["17", "20"]:
            if settings["compiler.version"] == "7" and std == "20":
                continue
            new_settings = settings
            new_settings["cppstd"] = std
            new_builds.append([new_settings, options, env_vars, build_requires])
    builder.builds = new_builds
    builder.run()
