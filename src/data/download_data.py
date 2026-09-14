import logging
import os
import urllib.request
import zipfile

logging.basicConfig(level=logging.INFO)


def download_and_extract_uci_power(data_dir: str):
    """
    Descarga el dataset público de consumo eléctrico de UCI.
    Este será uno de nuestros inputs ambientales para la microred.
    """
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00235/household_power_consumption.zip"
    os.makedirs(data_dir, exist_ok=True)
    zip_path = os.path.join(data_dir, "household_power_consumption.zip")

    if not os.path.exists(zip_path):
        logging.info(f"Descargando datos desde {url}...")
        urllib.request.urlretrieve(url, zip_path)
        logging.info("Descarga completada.")
    else:
        logging.info("El archivo zip ya existe. Saltando descarga.")

    csv_path = os.path.join(data_dir, "household_power_consumption.txt")
    if not os.path.exists(csv_path):
        logging.info("Extrayendo archivo...")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(data_dir)
        logging.info("Extracción completada.")


if __name__ == "__main__":
    RAW_DATA_DIR = os.path.join(os.path.dirname(__file__), "../../data/raw")
    download_and_extract_uci_power(RAW_DATA_DIR)
