(* Assumption: there are no duplicated words *)

type 'a tree = Empty | Cons of 'a tree * 'a * 'a tree

let str_list = ref []

(* hash function for hash tree *)
let hash_function (str: string): int =
  (String.length str) mod 26

(* Converts a string to a char list *)
let rec explode : string -> char list = function
  | "" -> []
  | s  -> String.get s 0 :: explode (String.sub s 1 ((String.length s) - 1))

(* Converts a char list to a string *)
let rec implode : char list -> string = function
  | [] -> ""
  | c::cs -> String.make 1 c ^ implode cs

(* returns the tree in the given index. The idx must follow the list indexing *)
let rec get_idx (idx: int) (lst: 'a tree list) : 'a tree =
  match lst with
  | [] -> failwith "the list is empty"
  | x::xs -> if idx > 0
             then get_idx (idx-1) xs
             else x

(* Adds the string in the tree *)
let rec add_string_to_tree (str: string) (tree: 'a tree): 'a tree =
  match tree with
  | Empty -> Cons (Empty, str, Empty)
  | Cons (t1, st, t2) -> if str < st
                         then Cons (add_string_to_tree str t1, st, t2)
                         else if str > st
                         then Cons (t1, st, add_string_to_tree str t2)
                         else tree

let rec set_list (str: string) (idx: int) (lst: 'a tree list): 'a tree list =
  match lst with
  | [] -> []
  | tree::trees -> if idx > 0
             then tree :: (set_list str (idx-1) trees)
             else if idx = 0
             then (add_string_to_tree str tree) :: trees
             else failwith " index is out of bounds "

(* Removes the element inside the list *)
let rec remove_elem (elem: char) (lst: char list) : char list =
  match lst with
  | [] -> []
  | x::xs ->
    if x = elem then xs
    else x :: (remove_elem elem xs)

let read_file (filename:string) : 'a tree list =
  (* Initializes the hash tree *)
  let rec init_hash (accum: 'a tree list) (count: int): 'a tree list =
    if count = 0
    then accum
    else init_hash (accum@[Empty]) (count-1)

  (* Gets the word per line in the file and store it in a list and in a tree *)
  in let rec read_lines channel sofar =
    try
      let ln = input_line channel
      in match implode (remove_elem '\r' (explode ln)) with
         | ln when ln <> "" -> str_list := ln::!str_list;
                               if List.mem 'q' (explode ln) && List.mem 'u' (explode ln)
                               then read_lines channel (set_list ln ((hash_function ln)-1) sofar)
                               else read_lines channel sofar
         | _ -> read_lines channel sofar
    with
    | End_of_file -> sofar
    | e -> raise e
  in
  try
    let channel = open_in filename
    in read_lines channel (init_hash [] 26)
  with
  | e -> raise e

(* Assuming w1 and w2 have the same length *)
let rec qu_check_words (w1: char list) (w2: char list): bool =
  match w1 with
  | [] -> true
  | x::xs ->
    if List.mem x w2
    then qu_check_words xs (remove_elem x w2)
    else false

let rec string_match (base: 'b)
                     (str: 'a)
                     (func: 'a -> 'a -> 'b -> 'b -> 'b)
                     (hash: 'a tree)
                     : 'b =
    match hash with
    | Empty -> base
    | Cons (t1, st, t2) -> func str st
                           (string_match base str func t1)
                           (string_match base str func t2)


let qu_quiz (filename: string): (string * string) list =
  let rec solve_quiz (lst: string list)
                     (hash: string tree list)
                     (accum: (string * string) list)
                     : (string * string) list =

    match lst with
    | [] -> str_list := []; accum
    | word::words ->
      let func (str: 'a) (elem: 'a) (t1: string) (t2: string): string =
          if qu_check_words (explode str) (explode elem)
          then elem
          else "" ^ t1 ^ t2

      in let word_qu = string_match "" (word^"qu") func (get_idx ((hash_function (word^"qu"))-1) hash)
      in if word_qu <> ""
      then solve_quiz words hash (accum @ [(word, word_qu)])
      else solve_quiz words hash accum

  in solve_quiz (List.rev !str_list) (read_file filename) []
