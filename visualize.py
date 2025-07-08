import matplotlib.pyplot as plt

from src.ramwich.stats import StatsDict


def collect_data(stats_dict: StatsDict):
    """
    Collect data from the RAMwich simulation statistics for visualization.
    """
    area_data = {}
    dynamic_energy_data = {}
    leakage_energy_data = {}
    activation_data = {}

    for key, value in stats_dict.items():
        if value.area > 0:
            area_data[key] = value.area

        if value.dynamic_energy > 0:
            dynamic_energy_data[key] = value.dynamic_energy

        if value.leakage_energy > 0:
            leakage_energy_data[key] = value.leakage_energy

        if value.activation_count > 0:
            activation_data[key] = value.activation_count

    return area_data, dynamic_energy_data, leakage_energy_data, activation_data


def visualize_area(area_data):
    """
    Visualize the area statistics from the RAMwich simulation.
    """
    total_area = sum(area_data.values())

    main_components = {}
    others = 0
    for key, value in area_data.items():
        if (value / total_area) >= 0.03:
            main_components[key] = value
        else:
            others += value

    if others > 0:
        main_components["Others"] = others

    plt.figure(figsize=(12, 8))
    wedges, texts, autotexts = plt.pie(
        main_components.values(),
        labels=None,
        autopct="%1.1f%%",
        startangle=140,
        colors=plt.cm.tab20.colors,
        pctdistance=0.85,
    )

    labels = [f"{key} ({value:.3f} mm²)" for key, value in main_components.items()]
    plt.legend(wedges, labels, title="Components", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    for autotext in autotexts:
        autotext.set_text(autotext.get_text().replace(".0%", "%"))

    plt.title("Area Distribution of RAMwich Components")
    plt.tight_layout()
    import os
    os.makedirs("./figures", exist_ok=True)
    plt.savefig("./figures/area_pie.png")

    sorted_items = sorted(area_data.items(), key=lambda x: x[1], reverse=True)
    top_items = sorted_items[:8]
    sorted_keys = [item[0] for item in top_items]
    sorted_values = [item[1] for item in top_items]

    plt.figure(figsize=(12, 8))
    bars = plt.bar(sorted_keys, sorted_values, color="skyblue")
    plt.title("Top 8 Components by Area")
    plt.xlabel("Components")
    plt.ylabel("Area (mm²)")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0, height + 0.05, f"{height:.3f}", ha="center", va="bottom", rotation=0
        )

    max_height = max(sorted_values)
    plt.ylim(0, max_height * 1.15)

    plt.subplots_adjust(bottom=0.3)
    plt.tight_layout()
    plt.savefig("./figures/area_bar.png")


def visualize_energy(dynamic_energy_data, leakage_energy_data):
    """
    Visualize the energy statistics from the RAMwich simulation.
    """

    total_dynamic = sum(dynamic_energy_data.values())
    main_dynamic = {}
    others_dynamic = 0

    for key, value in dynamic_energy_data.items():
        if (value / total_dynamic) >= 0.03:
            main_dynamic[key] = value
        else:
            others_dynamic += value

    if others_dynamic > 0:
        main_dynamic["Others"] = others_dynamic

    plt.figure(figsize=(12, 8))
    wedges, texts, autotexts = plt.pie(
        main_dynamic.values(),
        labels=None,
        autopct="%1.1f%%",
        startangle=140,
        colors=plt.cm.tab20.colors,
        pctdistance=0.85,
    )

    labels = [f"{key} ({value:.2f} pJ)" for key, value in main_dynamic.items()]
    plt.legend(wedges, labels, title="Components", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    for autotext in autotexts:
        autotext.set_text(autotext.get_text().replace(".0%", "%"))

    plt.title("Dynamic Energy Distribution of RAMwich Components")
    plt.tight_layout()
    plt.savefig("./figures/dynamic_energy_pie.png")

    sorted_dynamic = sorted(dynamic_energy_data.items(), key=lambda x: x[1], reverse=True)
    top_dynamic = sorted_dynamic[:8]
    dynamic_keys = [item[0] for item in top_dynamic]
    dynamic_values = [item[1] for item in top_dynamic]

    plt.figure(figsize=(12, 8))
    bars = plt.bar(dynamic_keys, dynamic_values, color="orange")
    plt.title("Top 8 Components by Dynamic Energy")
    plt.xlabel("Components")
    plt.ylabel("Dynamic Energy (pJ)")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0, height * 1.03, f"{height:.2f}", ha="center", va="bottom", rotation=0
        )

    max_height = max(dynamic_values)
    plt.ylim(0, max_height * 1.15)

    plt.subplots_adjust(bottom=0.3)
    plt.tight_layout()
    plt.savefig("./figures/dynamic_energy_bar.png")

    total_leakage = sum(leakage_energy_data.values())
    main_leakage = {}
    others_leakage = 0

    for key, value in leakage_energy_data.items():
        if (value / total_leakage) >= 0.03:
            main_leakage[key] = value
        else:
            others_leakage += value

    if others_leakage > 0:
        main_leakage["Others"] = others_leakage

    plt.figure(figsize=(12, 8))
    wedges, texts, autotexts = plt.pie(
        main_leakage.values(),
        labels=None,
        autopct="%1.1f%%",
        startangle=140,
        colors=plt.cm.tab20.colors,
        pctdistance=0.85,
    )

    labels = [f"{key} ({value:.2f} pJ)" for key, value in main_leakage.items()]
    plt.legend(wedges, labels, title="Components", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    for autotext in autotexts:
        autotext.set_text(autotext.get_text().replace(".0%", "%"))

    plt.title("Leakage Energy Distribution of RAMwich Components")
    plt.tight_layout()
    plt.savefig("./figures/leakage_energy_pie.png")

    sorted_leakage = sorted(leakage_energy_data.items(), key=lambda x: x[1], reverse=True)
    top_leakage = sorted_leakage[:8]
    leakage_keys = [item[0] for item in top_leakage]
    leakage_values = [item[1] for item in top_leakage]

    plt.figure(figsize=(12, 8))
    bars = plt.bar(leakage_keys, leakage_values, color="skyblue")
    plt.title("Top 8 Components by Leakage Energy")
    plt.xlabel("Components")
    plt.ylabel("Leakage Energy (pJ)")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0, height * 1.03, f"{height:.2f}", ha="center", va="bottom", rotation=0
        )

    max_height = max(leakage_values)
    plt.ylim(0, max_height * 1.15)

    plt.subplots_adjust(bottom=0.3)
    plt.tight_layout()
    plt.savefig("./figures/leakage_energy_bar.png")


def visualize_activation_count(activation_data):
    """
    Visualize the activation count statistics from the RAMwich simulation.
    """

    total_activations = sum(activation_data.values())
    main_activations = {}
    others_activations = 0

    for key, value in activation_data.items():
        if (value / total_activations) >= 0.03:
            main_activations[key] = value
        else:
            others_activations += value

    if others_activations > 0:
        main_activations["Others"] = others_activations

    plt.figure(figsize=(12, 8))
    wedges, texts, autotexts = plt.pie(
        main_activations.values(),
        labels=None,
        autopct="%1.1f%%",
        startangle=140,
        colors=plt.cm.tab20.colors,
        pctdistance=0.85,
    )

    labels = [f"{key} ({int(value)} times)" for key, value in main_activations.items()]
    plt.legend(wedges, labels, title="Components", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    for autotext in autotexts:
        autotext.set_text(autotext.get_text().replace(".0%", "%"))

    plt.title("Activation Count Distribution of RAMwich Components")
    plt.tight_layout()
    plt.savefig("./figures/activation_count_pie.png")

    sorted_activations = sorted(activation_data.items(), key=lambda x: x[1], reverse=True)
    top_activations = sorted_activations[:8]
    activation_keys = [item[0] for item in top_activations]
    activation_values = [item[1] for item in top_activations]

    plt.figure(figsize=(12, 8))
    bars = plt.bar(activation_keys, activation_values, color="salmon")
    plt.title("Top 8 Components by Activation Count")
    plt.xlabel("Components")
    plt.ylabel("Activation Count (times)")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0, height * 1.03, f"{int(height)}", ha="center", va="bottom", rotation=0
        )

    max_height = max(activation_values)
    plt.ylim(0, max_height * 1.15)

    plt.subplots_adjust(bottom=0.3)
    plt.tight_layout()
    plt.savefig("./figures/activation_count_bar.png")


def visualize_stats(stats: StatsDict):
    """
    Visualize the statistics from the RAMwich simulation.
    """
    area_data, dynamic_energy_data, leakage_energy_data, activation_data = collect_data(stats)

    visualize_area(area_data)
    visualize_energy(dynamic_energy_data, leakage_energy_data)
    visualize_activation_count(activation_data)
