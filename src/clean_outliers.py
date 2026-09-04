import os
import pandas as pd
import numpy as np


def apply_outlier_filters():
    raw_data_path = os.path.join("data", "raw_business_data.csv")
    cleaned_output_path = os.path.join("data", "cleaned_business_data.csv")

    if not os.path.exists(raw_data_path):
        raise FileNotFoundError(
            "[-] Raw data missing. Run 'python data/download_data.py' first."
        )

    df = pd.read_csv(raw_data_path)
    initial_count = len(df)

    target_col = "Density"

    Q1 = df[target_col].quantile(0.25)
    Q3 = df[target_col].quantile(0.75)
    IQR = Q3 - Q1

    iqr_lower_bound = Q1 - 1.5 * IQR
    iqr_upper_bound = Q3 + 1.5 * IQR

    cleaned_df = df[
        (df[target_col] >= iqr_lower_bound)
        & (df[target_col] <= iqr_upper_bound)
    ].copy()

    removed_count = initial_count - len(cleaned_df)

    cleaned_df.to_csv(cleaned_output_path, index=False)

    print("===================================================")
    print("          PRODUCTION OUTLIER FILTERING REPORT")
    print("===================================================")
    print(f"Target Feature Filtered: {target_col}")
    print(f"Initial Dataset Records: {initial_count:,}")
    print(
        f"Tukey IQR Valid Range: "
        f"[{iqr_lower_bound:,.2f}, {iqr_upper_bound:,.2f}]"
    )
    print(
        f"Outlier Records Removed: {removed_count:,} "
        f"({removed_count / initial_count * 100:.2f}%)"
    )
    print(f"Final Cleaned Records: {len(cleaned_df):,}")
    print(
        f"\n[+] Saved cleaned dataset artifact to: "
        f"{cleaned_output_path}"
    )


if __name__ == "__main__":
    apply_outlier_filters()