package com.api.controller;

import com.api.model.Item;
import com.api.repository.ItemRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/itens")
public class ItemController {

    private final ItemRepository repository;

    public ItemController(ItemRepository repository) {
        this.repository = repository;
    }

    // GET /itens - lista todos os itens
    @GetMapping
    public List<Item> listar() {
        return repository.findAll();
    }

    // POST /itens - cria um novo item
    @PostMapping
    public ResponseEntity<Item> criar(@RequestBody Item item) {
        Item salvo = repository.save(item);
        return ResponseEntity.status(201).body(salvo);
    }

    // DELETE /itens/{id} - remove um item pelo id
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deletar(@PathVariable Long id) {
        if (!repository.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        repository.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}
