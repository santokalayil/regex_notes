import pandas as pd
import re
import numpy as np

# these patterns are used to find phonenumbers, upi id etc from tweets
phonenumber_pattern = r"\+\d{2}[ -]?\d{5}[ -]?\d{5}" # +91 etc are taken here
phonenumber_pattern = r"[📞\s][0 ]{0,1}[6789]\d{9}\b" 

hashtag_pattern = r"#[a-zA-Z0-9_]+"
username_pattern = r"[\s, .]@[a-zA-Z0-9_]+[\s,]{0,1}"  # @SantoKalayil 
vpa_pattern  = r"\w[\w-]+\w@[a-zA-Z]{3,10}[\s,]"
email_pattern = r"\w+[_\.\+]*\w+@[a-zA-Z]{3,10}[.][a-z]+[.]*[a-z]*[ ,]*"



# phone numbers
def find_phone_numbers(txt):  # bug --> 8891123220@paytm upi's number will be extracted
    if txt in [np.NaN, None, ""]:
        return []
    else:
        results = re.findall(r"\+\d{2}[ -]?\d{5}[ -]?\d{5}", txt) # +91 etc are taken here
        possible_phs = re.findall(r"[📞\s][0 ]{0,1}[6789]\d{9}\b", txt) # getting ph from ";k;k; dgd 08812334560 9961212345 okok"
        results2 = [ph.strip().lstrip("📞") for ph in possible_phs]
        # removing duplicates if like this: ['9512345678', '+91 9512345678']
        for number_without_plus in list(results2):
            for number_with_plus in results:
                if number_without_plus in number_with_plus:
                    try:
                        results2.remove(number_without_plus)
                    except Exception as e:
                        print(f"Error: {e}")
                        pass

        results_all = results2 +results
        return results_all

# function created for removing duplicate codes in the coming functions
def is_not_digits_only(t, symbol_before):
    try:
        int(t.lstrip(symbol_before))
        return False
    except:
        return True

# hashtags
def find_hashtags(txt):
    global is_not_digits_only
    if txt in [np.NaN, None, ""]:
        return []
    else:
        results = re.findall(r"#[a-zA-Z0-9_]+", txt) # +91 etc are taken here
        return [ht.strip() for ht in results if is_not_digits_only(ht, symbol_before="#")]



# @ mentions
def find_ats(txt):
    global is_not_digits_only
    if txt in [np.NaN, None, ""]:
        return []
    else:
        results = re.findall(r"[\s, .]@[a-zA-Z0-9_]+[\s,]{0,1}", txt)  # before @ there can be only /s or , or . also in the end only space or comma

                
        # striping out spaace and comma which are put in end of regex expression
        results = [t.strip().rstrip(",") for t in results]
        out = [t for t in results if is_not_digits_only(t, symbol_before="@")]
        return out

# vpas
def find_vpas(txt):
    global is_not_digits_only
    if txt in [np.NaN, None, ""]:
        return []
    else:
        # contains alphabets only in right side of @. left side can be alphanumeric; also inbetween a dash(-) can also come
        results = re.findall(r"\w[\w-]+\w@[a-zA-Z]{3,10}[\s,]", txt)  # space , comma will be valid if ther is}"

        # striping out 
        results = [t.strip().rstrip(",") for t in results]
        return results

# EMAIL -----
# link to rules
# https://help.returnpath.com/hc/en-us/articles/220560587-What-are-the-rules-for-email-address-syntax-
def find_emails(txt):
    global is_not_digits_only
    if txt in [np.NaN, None, ""]:
        return []
    else:
        results = re.findall(r"\w+[_\.\+]*\w+@[a-zA-Z]{3,10}[.][a-z]+[.]*[a-z]*[ ,]*", txt)  # space , comma will be valid if ther is}"

        # striping out 
        results = [t.strip().rstrip(",") for t in results]
        return results
      
      
def create_new_twitter_df_columns(df: pd.DataFrame, tweet_column="text") -> pd.DataFrame:
    # make sure that full_text column is in input dataframe
    df["found_ph"] = df[tweet_column].apply(lambda txt: find_phone_numbers(txt))
    df["found_vpa"] = df[tweet_column].apply(lambda txt: find_vpas(txt))
    df["found_email"] = df[tweet_column].apply(lambda txt: find_emails(txt))
    df["found_hashtag"] = df[tweet_column].apply(lambda txt: find_hashtags(txt))
    df["found_at"] = df[tweet_column].apply(lambda txt: find_ats(txt))
    return df
  
 
if __name__ == "__main__":
    pass
