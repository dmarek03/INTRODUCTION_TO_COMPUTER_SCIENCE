"""
Zadanie 18. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla nałożono
dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na polu
na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu (np. narożnika)
król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica T[8][8] wypełniona
liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne w=0 i k=0.
Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego narożnika.
"""