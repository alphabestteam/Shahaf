import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DessertsRecipesComponent } from './desserts-recipes.component';

describe('DessertsRecipesComponent', () => {
  let component: DessertsRecipesComponent;
  let fixture: ComponentFixture<DessertsRecipesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DessertsRecipesComponent]
    });
    fixture = TestBed.createComponent(DessertsRecipesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
