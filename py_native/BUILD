filegroup(
    name = "srcs",
    srcs = glob(["*.py"]) + [
        "BUILD",
        "//py_native/fibonacci:srcs",
    ],
)

py_binary(
    name = "bin",
    srcs = ["bin.py"],
    deps = [
        ":lib",
        "//py_native/fibonacci",
    ],
)

py_library(
    name = "lib",
    srcs = ["lib.py"],
)

py_test(
    name = "test",
    srcs = ["test.py"],
    deps = [
        ":lib",
        "//py_native/fibonacci",
    ],
)

py_test(
    name = "fail",
    srcs = ["fail.py"],
    deps = [":lib"],
)