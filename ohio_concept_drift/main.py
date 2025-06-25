from ohio_concept_drift import resources


def run():
    ohio_df = resources.load_ohio_arff()
    print(ohio_df.head())
    print("Echo")
