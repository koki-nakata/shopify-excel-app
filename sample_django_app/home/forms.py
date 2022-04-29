from django import forms

def widget(placeholder, classname, value):
    widget = forms.TextInput(
        attrs={
            'placeholder': placeholder,
            'class': classname,
            'value': value,
        }
    )
    return widget

class ImportForm(forms.Form):

    last_name = forms.CharField(label= "姓", widget=widget("姓", "Polaris-TextField__Input", "お名前(姓)"))
    first_name = forms.CharField(label= "名", widget=widget("名", "Polaris-TextField__Input", "お名前(名)"))
    email = forms.CharField(label="メールアドレス", widget=widget("メールアドレス", "Polaris-TextField__Input", "E-MAIL"))
    company = forms.CharField(label="会社名", widget=widget("会社名", "Polaris-TextField__Input", "会社名"))
    address1 = forms.CharField(label="住所1", widget=widget("住所1", "Polaris-TextField__Input", "住所1"))
    address2 = forms.CharField(label="住所2", widget=widget("住所2", "Polaris-TextField__Input", "住所2"))
    city = forms.CharField(label="市区町村", widget=widget("市区町村", "Polaris-TextField__Input", "市区町村"))
    province = forms.CharField(label="都道府県", widget=widget("都道府県", "Polaris-TextField__Input", "都道府県"))
    province_code = forms.CharField(label="都道府県コード", widget=widget("都道府県コード", "Polaris-TextField__Input", "都道府県コード"))
    country = forms.CharField(label="国", widget=widget("国", "Polaris-TextField__Input", "国"))
    country_code = forms.CharField(label="国コード", widget=widget("国コード", "Polaris-TextField__Input", "国コード"))
    zip1 = forms.CharField(label="郵便番号1", widget=widget("郵便番号1", "Polaris-TextField__Input", "郵便番号1"))
    zip2 = forms.CharField(label="郵便番号2", widget=widget("郵便番号2", "Polaris-TextField__Input", "郵便番号2"))
    phone1 = forms.CharField(label="電話番号1", widget=widget("電話番号1", "Polaris-TextField__Input", "TEL1"))
    phone2 = forms.CharField(label="電話番号2", widget=widget("電話番号2", "Polaris-TextField__Input", "TEL2"))
    phone3 = forms.CharField(label="電話番号3", widget=widget("電話番号3", "Polaris-TextField__Input", "TEL3"))
    accepts_email_marketing	= forms.CharField(label="メールマーケティングの許可", widget=widget("名", "Polaris-TextField__Input", "メールマーケティング"))
    accepts_sms_marketing	= forms.CharField(label="SMSマーケティングの許可", widget=widget("名", "Polaris-TextField__Input", "SMSマーケティング"))
    tags = forms.CharField(label="顧客タグ", widget=widget("タグ", "Polaris-TextField__Input", "タグ"))
    note = forms.CharField(label="顧客メモ", widget=widget("メモ", "Polaris-TextField__Input", "メモ"))
    tax_exempt = forms.CharField(label="非課税対象", widget=widget("非課税対象", "Polaris-TextField__Input", "非課税対象"))
    file = forms.FileField(label="CSVファイルアップロード")
