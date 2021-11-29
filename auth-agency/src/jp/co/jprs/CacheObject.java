package jp.co.jprs;

import java.io.Serializable;
import java.util.List;
import java.util.Map;

public class CacheObject implements Serializable {
    /** serialVersionUID */
    private static final long serialVersionUID = 1L;

    /** ヘッダー */
    private  Map<String,List<String>> headers;

    /** ボディ */
    private  String body;

    /**
     * ヘッダーを取得。
     *
     * @return ヘッダー
     */
    public Map<String,List<String>> getHeaders() {
        return headers;
    }

    /**
     * ヘッダーを設定。
     *
     * @param headers ヘッダー
     */
    public void setHeaders(Map<String,List<String>> headers) {
        this.headers = headers;
    }

    /**
     * ボディを取得。
     *
     * @return ボディ
     */
    public String getBody() {
        return body;
    }

    /**
     * ボディを設定。
     *
     * @param body ボディ
     */
    public void setBody(String body) {
        this.body = body;
    }
}
