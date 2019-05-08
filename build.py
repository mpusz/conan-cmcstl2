from cpt.packager import ConanMultiPackager
import copy

if __name__ == "__main__":
    builder = ConanMultiPackager(
        # package id
        username = "mpusz",
        channel = "testing",
        
        # dependencies
        remotes = None,
        build_policy = None,
        upload_dependencies=False,

        # build configurations
        archs = ["x86_64"],

        # package upload (REMEMBER to set CONAN_PASSWORD environment variable in Travis CI and AppVeyor)
        login_username = "mpusz",
        upload = "https://api.bintray.com/conan/mpusz/conan-mpusz"
    )        
    builder.add_common_builds(pure_c=False)
    new_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        for std in ["17", "20"]:
            if settings["compiler.version"] == "7" and std == "20":
                continue
            new_settings = copy.copy(settings)
            new_settings["compiler.cppstd"] = std
            new_builds.append([new_settings, options, env_vars, build_requires])
    builder.builds = new_builds
    builder.run()
