---
title: "Excel to PatternLislinlist"
date: 2023-06-13T23:35:16+09:00
categories : [""]
tags : ["",""]
draft: true
---

# Excel to PatternLislinlist

## 概要

[パターンに応じてファイルソートする](./regax-file-sorting.md)仕組みを使う際に面倒なパターンリストの作成を
Excelで管理できるようにするための仕組みを考える

## サンプルコード

実際に特定列に記述された正規表現と各フラグに応じて記述する処理とする

単純に3列の情報を文字列として出力しているのみなので、Excel側で出力させる情報はきちんと管理する。

``` VB

Sub createPythonList()

    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Sheet1") ' シート名を適宜変更してください
    
    Dim lastRow As Long
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row

    Dim listFile As Integer
    listFile = FreeFile

    Open "pattern_list.py" For Output As listFile
    Print #listFile, "pattern_list = ["
    
    Dim i As Long
    For i = 2 To lastRow
        Dim regex As String
        Dim fileFlag As String
        Dim dirFlag As String
        
        regex = ws.Cells(i, 1)
        fileFlag = ws.Cells(i, 2)
        dirFlag = ws.Cells(i, 3)
        
        Print #listFile, "    (""" & regex & """, " & fileFlag & ", " & dirFlag & "),"
    Next i
    
    Print #listFile, "]"
    Close listFile

End Sub
```