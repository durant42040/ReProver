file_path = "data/leandojo_benchmark_4/novel_premises/train.json"

with open(file_path, "r") as file:
    content = file.read()

content = content.replace(
    "/scratch/10710/rhsiang/lean_dojo/leanprover-community-mathlib4-c44e0c8ee63ca166450922a373c7409c5d26b00b/mathlib4",
    "https://github.com/leanprover-community/mathlib4"
)

with open(file_path, "w") as file:
    file.write(content)

file_path = "data/leandojo_benchmark_4/random/train.json"

with open(file_path, "r") as file:
    content = file.read()

content = content.replace(
    "/scratch/10710/rhsiang/lean_dojo/leanprover-community-mathlib4-c44e0c8ee63ca166450922a373c7409c5d26b00b/mathlib4",
    "https://github.com/leanprover-community/mathlib4"
)

with open(file_path, "w") as file:
    file.write(content)

file_path = "data/leandojo_benchmark_4/novel_premises/val.json"

with open(file_path, "r") as file:
    content = file.read()

content = content.replace(
    "/scratch/10710/rhsiang/lean_dojo/leanprover-community-mathlib4-c44e0c8ee63ca166450922a373c7409c5d26b00b/mathlib4",
    "https://github.com/leanprover-community/mathlib4"
)

with open(file_path, "w") as file:
    file.write(content)

file_path = "data/leandojo_benchmark_4/random/val.json"

with open(file_path, "r") as file:
    content = file.read()

content = content.replace(
    "/scratch/10710/rhsiang/lean_dojo/leanprover-community-mathlib4-c44e0c8ee63ca166450922a373c7409c5d26b00b/mathlib4",
    "https://github.com/leanprover-community/mathlib4"
)

with open(file_path, "w") as file:
    file.write(content)


file_path = "data/leandojo_benchmark_4/novel_premises/test.json"

with open(file_path, "r") as file:
    content = file.read()

content = content.replace(
    "/scratch/10710/rhsiang/lean_dojo/leanprover-community-mathlib4-c44e0c8ee63ca166450922a373c7409c5d26b00b/mathlib4",
    "https://github.com/leanprover-community/mathlib4"
)

with open(file_path, "w") as file:
    file.write(content)

file_path = "data/leandojo_benchmark_4/random/test.json"

with open(file_path, "r") as file:
    content = file.read()

content = content.replace(
    "/scratch/10710/rhsiang/lean_dojo/leanprover-community-mathlib4-c44e0c8ee63ca166450922a373c7409c5d26b00b/mathlib4",
    "https://github.com/leanprover-community/mathlib4"
)

with open(file_path, "w") as file:
    file.write(content)