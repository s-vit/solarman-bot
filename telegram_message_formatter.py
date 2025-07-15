
def make_report(stats: dict, date: str) -> str:
    keys = [
        ("GENERATE_VALUE", "🔆 Вироблено", "kWh"),
        ("USE_VALUE", "💡 Спожито", "kWh"),
        ("BUY_VALUE", "⚡️ Куплено", "kWh"),
        ("CHARGE_VALUE", "🔋⬆️ Заряд АКБ", "kWh"),
        ("DISCHARGE_VALUE", "🔋⬇️ Розряд АКБ", "kWh"),
        ("GENERATION_RATIO", "🏭 Використання мережі", "%"),
        ("PRE_INCOME(UAH)", "💵 Економія", "грн"),
    ]

    lines = [f"📊 Щоденний звіт за {date}\n"]
    for key, icon, unit in keys:
        value = stats.get(key)
        if value is not None:
            lines.append(f"{icon}: {value}{unit}")
    lines.append("\n#звіт_день")
    return "\n".join(lines)

def make_report_month(stats: dict) -> str:
    keys = [
        ("GENERATE_VALUE", "🔆 Вироблено", "kWh"),
        ("USE_VALUE", "💡 Спожито", "kWh"),
        ("BUY_VALUE", "⚡️ Куплено", "kWh"),
        ("CHARGE_VALUE", "🔋⬆️ Заряд АКБ", "kWh"),
        ("DISCHARGE_VALUE", "🔋⬇️ Розряд АКБ", "kWh"),
        ("GENERATION_RATIO", "🏭 Використання мережі", "%"),
        ("PRE_INCOME(UAH)", "💵 Економія", "грн"),
    ]

    lines = [f"📊 Щомісячний звіт за липень 2025\n"]
    for key, icon, unit in keys:
        value = stats.get(key)
        if value is not None:
            lines.append(f"{icon}: {value}{unit}")
    lines.append("\n#звіт_місяць")
    return "\n".join(lines)