import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ItalianRecipesComponent } from './italian-recipes.component';

describe('ItalianRecipesComponent', () => {
  let component: ItalianRecipesComponent;
  let fixture: ComponentFixture<ItalianRecipesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ItalianRecipesComponent]
    });
    fixture = TestBed.createComponent(ItalianRecipesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
