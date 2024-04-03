import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    """download stock prices from Yahoo Finance for a given year into a CSV file
    Parameters
    -----------
    year : int
        an integer with a four-digit year
    """
    tic = 'QAN.AX'
    start = f'{year}-01-01'
    end = f'{year}-12-31'
    pth = os.path.join(cfg.DATADIR,f'qan_prc_{year}.csv')
    df = yf_example2.yf_prc_to_csv(
        tic = tic,
        pth = pth,
        start = start,
        end = end
    )
if __name__ == "__main__":
    year = 2020,
    qan_prc_to_csv(year)
