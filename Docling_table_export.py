import logging
import time
from pathlib import Path
import pandas as pd
from docling.document_converter import DocumentConverter
_log = logging.getLogger(__name__)
def main():
    logging.basicConfig(level=logging.INFO)

    input_doc_path = Path("docs/Wolfspeed_C3M0016120K.pdf")
    output_dir = Path("scratch")
    docs_dir = Path("docs")

    doc_converter = DocumentConverter()

    start_time = time.time()

    conv_res = doc_converter.convert(input_doc_path)

    output_dir.mkdir(parents=True, exist_ok=True)

    doc_filename = conv_res.input.file.stem

    # Create/update a markdown file for the document
    md_output_path = docs_dir / f"{doc_filename}.md"
    
    with md_output_path.open("w") as md_file:
        md_file.write(f"# {doc_filename}\n\n")
        md_file.write(f"*Document converted on {time.strftime('%Y-%m-%d')}*\n\n")
        
        # Export tables
        for table_ix, table in enumerate(conv_res.document.tables):
            table_df: pd.DataFrame = table.export_to_dataframe()
            print(f"## Table {table_ix}")
            table_md = table_df.to_markdown()
            print(table_md)
            
            # Write table to markdown file
            md_file.write(f"## Table {table_ix + 1}\n\n")
            md_file.write(f"{table_md}\n\n")

            # Save the table as csv
            element_csv_filename = output_dir / f"{doc_filename}-table-{table_ix + 1}.csv"
            _log.info(f"Saving CSV table to {element_csv_filename}")
            table_df.to_csv(element_csv_filename)

            # Save the table as html
            element_html_filename = output_dir / f"{doc_filename}-table-{table_ix + 1}.html"
            _log.info(f"Saving HTML table to {element_html_filename}")
            with element_html_filename.open("w") as fp:
                fp.write(table.export_to_html(doc=conv_res.document))

    end_time = time.time() - start_time

    _log.info(f"Document converted and tables exported in {end_time:.2f} seconds.")
    _log.info(f"Markdown file saved to {md_output_path}")

if __name__ == "__main__":
    main()