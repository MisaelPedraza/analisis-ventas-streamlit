from pathlib import Path

import numpy as np
import pandas as pd


def main() -> None:
    rng = np.random.default_rng(42)
    dates = pd.date_range("2025-01-01", periods=90, freq="D")
    regions = ["Norte", "Centro", "Sur", "Occidente"]
    categories = ["Electrónica", "Hogar", "Oficina"]
    skus = [f"SKU-{number:03d}" for number in range(1, 21)]

    rows = []
    for date in dates:
        for region in regions:
            for category in categories:
                for sku in rng.choice(skus, size=4, replace=False):
                    units = int(rng.integers(1, 30))
                    unit_price = float(rng.integers(15, 250))
                    rows.append(
                        {
                            "date": date,
                            "region": region,
                            "category": category,
                            "sku": sku,
                            "units": units,
                            "revenue": round(units * unit_price, 2),
                        }
                    )

    output = Path(__file__).parent / "sales_daily.csv"
    pd.DataFrame(rows).to_csv(output, index=False)
    print(f"Datos creados en {output}")


if __name__ == "__main__":
    main()
