let crmUrl = 'http://127.0.0.1:8000';
let localUrl = 'http://127.0.0.1:8001';
// let crmUrl = 'http://crm.ikenguru.ru';
export default {
    marketToken:'!!!ken!!!guru!!',

    urls: {
        autocomplete: `${crmUrl}/api1/market/autocomplete`,
        localSetting: `${localUrl}/get_local_setting`,
    },

}